# 导入定义的索引类
from haystack import indexes
# 导入对应的模型类
from goods.models import GoodsSKU

# 指定对于某个类的某些数据建立索引
# 索引类名格式:模型类名+Index
class GoodsSKUIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段  use_tmeplate=True 指定根据表中的哪些字段建立索引文件的说明写入一个文件中
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        # 返回模型类
        return GoodsSKU

    # 建立索引数据
    def index_queryset(self, using=None):
        # 返会所有数据
        return self.get_model().objects.all()