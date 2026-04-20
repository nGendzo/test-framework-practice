export class CartPage {
  constructor(page) {
    this.page = page;

    this.checkoutButton = page.getByTestId('checkout');
  }

  async open() {
    await this.page.goto('https://www.saucedemo.com/cart.html');
  }

  async clickCheckoutButton() {
    await this.checkoutButton.click();
  }
}
