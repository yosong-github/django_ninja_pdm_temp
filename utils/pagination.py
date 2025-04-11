import math

from django.db.models import QuerySet
from django.forms import model_to_dict

from utils.api.response import PageListResponse


def paginate(page, page_size, data_orm: QuerySet) -> PageListResponse:
    total_count = data_orm.count()
    total_pages = math.ceil(total_count / page_size)

    data = {"total_pages": total_pages, "total": total_count, "page": page, "page_size": page_size, "list": []}

    if page <= total_pages:
        offset_value = (page - 1) * page_size
        limit_value = min(page_size, total_count - offset_value)
        data["list"] = [model_to_dict(item) for item in data_orm[offset_value : offset_value + limit_value]]

    return PageListResponse(data=data)
