#dasdasadasd
class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title_text = page.locator(".title")

    def get_title(self):
        return self.title_text.inner_text()
    
    
    