from aiohttp import web
import rapidjson as json
from rapidjson import DM_ISO8601, UM_CANONICAL
from webargs import fields, validate, missing
from webargs.aiohttpparser import use_kwargs

from ..models import Sport
from ..settings import manager


create_sport_category_args = {
    'name': fields.Str(required=True),
    'active': fields.Bool(missing=True),
}

update_sport_category_args = {
    'id': fields.Str(required=True, location='match_info'),
    'name': fields.Str(required=False),
    'active': fields.Bool(required=False),
}


async def get_sport_categories(request):
    sports = await manager.execute(Sport.select().where(Sport.active==True))
    results = [sport.to_dict() for sport in sports]
    return web.Response(
        text=json.dumps(results, indent=4, datetime_mode=DM_ISO8601, uuid_mode=UM_CANONICAL),
        content_type='application/json',
        charset='utf-8',
    )


@use_kwargs(create_sport_category_args)
async def create_sport_category(request, name, active):
    sport = await manager.create(Sport, name=name, active=active)
    result = sport.to_dict()
    return web.Response(
        text=json.dumps(result, indent=4, datetime_mode=DM_ISO8601, uuid_mode=UM_CANONICAL),
        content_type='application/json',
        charset='utf-8'
    )


@use_kwargs(update_sport_category_args)
async def update_sport_category(request, id, name, active):
    sport = await manager.get(Sport, uid=id)
    if name is not missing:
        sport.name = name
    if active is not missing:
        sport.active = active

    if sport.dirty_fields:
        await manager.update(sport)

    result = sport.to_dict()
    return web.Response(
        text=json.dumps(result, indent=4, datetime_mode=DM_ISO8601, uuid_mode=UM_CANONICAL),
        content_type='application/json',
        charset='utf-8'
    )


def setup_routes(app):
    app.router.add_route('GET', '/sport', get_sport_categories)
    app.router.add_route('POST', '/sport', create_sport_category)
    app.router.add_route('POST', '/sport/{id}', update_sport_category)
