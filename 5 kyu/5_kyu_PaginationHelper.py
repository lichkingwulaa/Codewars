"""
https://www.codewars.com/kata/paginationhelper/train/python
"""
class PaginationHelper:
	"""分页管理助手"""
	# The constructor takes in an array of items and a integer indicating
	# how many items fit within a single page
	def __init__(self, collection, items_per_page):
		"""初始化，项目的总数量以及每页项目数量"""
		self.collection = collection
		self.items_per_page = items_per_page
	
	# returns the number of items within the entire collection
	def item_count(self):
		"""返回项目的总数量"""
		return len(self.collection)
	
	# returns the number of pages
	def page_count(self):
		"""返回页码数"""
		return int((len(self.collection)-1)/self.items_per_page) + 1
	
	# returns the number of items on the current page. page_index is zero based
	# this method should return -1 for page_index values that are out of range
	def page_item_count(self, page_index):
		"""计算某页的项目数"""
		page = int((len(self.collection)-1)/self.items_per_page)
		if page_index < page:
			return self.items_per_page
		elif page_index == page:
			return len(self.collection) - page_index * self.items_per_page
		else:
			return -1
	
	# determines what page an item is on. Zero based indexes.
	# this method should return -1 for item_index values that are out of range
	def page_index(self, item_index):
		"""计算某个项目的页码"""
		if 0 <= item_index < len(self.collection):
			return int(item_index / self.items_per_page)
		else:
			return -1