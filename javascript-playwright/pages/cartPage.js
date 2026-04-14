export class CartPage {
  constructor(page) {
    this.page = page;

    this.itemListNames = page.getByTestId('inventory-item-name');
  }

  async open() {
    await this.page.goto('https://www.saucedemo.com/cart.html');
  }
}
