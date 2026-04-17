export class ProductPage {
  constructor(page) {
    this.page = page;

    this.addToCartButton = page.getByTestId('add-to-cart');
    this.cartPageButton = page.getByTestId('shopping-cart-link');
  }

  async open(itemId) {
    await this.page.goto(
      `https://www.saucedemo.com/inventory-item.html?id=${itemId}`,
    );
  }

  async addToCart() {
    await this.addToCartButton.click();
  }

  async openCartPage() {
    await this.cartPageButton.click();
  }
}
