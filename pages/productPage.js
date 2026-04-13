export class ProductPage {
  constructor(page) {
    this.page = page;

    this.addToCartButton = page.getByTestId('add-to-cart');
  }

  async open(itemId) {
    await this.page.goto(
      `https://www.saucedemo.com/inventory-item.html?id=${itemId}`,
    );
  }

  async addToCart() {
    await this.addToCartButton.click();
  }
}
