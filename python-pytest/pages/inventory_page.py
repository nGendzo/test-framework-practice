class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title_text = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")

    def get_title(self):
        return self.title_text.inner_text()
    
    def get_items_count(self):
        return self.inventory_items.count()

    def open_item(self, item_name):
        self.page.get_by_text(item_name).click()
    
    