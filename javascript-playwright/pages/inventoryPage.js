export class InventoryPage {
  constructor(page) {
    this.page = page;

    this.burgerMenuButton = page.locator('#react-burger-menu-btn');
    this.burgerMenuItemList = page.getByRole('link', { name: 'All Items' });
    this.addToCartButton = page.getByTestId('add-to-cart');
    this.cartLink = page.getByTestId('shopping-cart-link');
    this.itemListNames = page.getByTestId('inventory-item-name');
  }

  async open() {
    await this.page.goto('https://www.saucedemo.com/inventory.html');
  }

  async openBurgerMenu() {
    await this.burgerMenuButton.click();
  }

  async openItem(name) {
    await this.itemListNames.filter({ hasText: name }).click();
  }

  async addToCart() {
    await this.addToCartButton.click();
  }

  async goToCart() {
    await this.cartLink.click();
  }
}
