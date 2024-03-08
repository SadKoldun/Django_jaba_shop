from goods.views import Product

from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline


def q_search(query):
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)

    result = Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')
    result = result.annotate(
        headline=SearchHeadline(
            'name',
            query,
            start_sel='<span style="background-color: grey;">',
            stop_sel='</span>',
        )
    )

    return result
