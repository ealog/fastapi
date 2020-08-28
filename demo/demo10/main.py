# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2020/8/28 2:26 下午
#       @Author  : cxy =.=
#       @File    : main.py
#       @Software: PyCharm
#       @Desc    :
# ---------------------------------------------
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: str,
        size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
