export class ProductPage {
  constructor(page) {
    this.page = page;

    this.addToCartButton = page.getByTestId('add-to-cart');
    this.cartPageButton = page.getByTestId('shopping-cart-link');
    this.burgerMenuButton = page.locator('#react-burger-menu-btn');
    this.inventoryPageButton = page.getByTestId('inventory-sidebar-link');
  }

  async open(itemId) {
    await this.page.goto(
      `https://www.saucedemo.com/inventory-item.html?id=${itemId}`,
    );
  }

  async addToCart() {
    await this.addToCartButton.click();
  }

  async openCart() {
    await this.cartPageButton.click();
  }

  async openBurgerMenu() {
    await this.burgerMenuButton.click();
  }

  async openInventoryPage() {
    this.inventoryPageButton.click();
  }

  async goToInventory() {
    await this.openBurgerMenu();
    await this.openInventoryPage();
  }
}
