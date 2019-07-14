from django.template.response import TemplateResponse

from shop.models import Product


def list_view(request):
    # 建立一个字典对象，类似java中的map对象，用来存放相应的数据，后续要放到模板文件中去
    ctx = {}
    # 通过django的orm模型，从数据库访问数据
    product_list = Product.objects.filter(is_publish=True)

    # 将数据库查询到的数据，放到字典对象中去，名称叫做'product_list'，后续在模板中可以用这个名称来访问这个对象
    ctx['product_list'] = product_list

    # 调用django的TemplateResponse，将数据加载到模板中的对应位置
    return TemplateResponse(request, 'client/product_list.html', ctx)
