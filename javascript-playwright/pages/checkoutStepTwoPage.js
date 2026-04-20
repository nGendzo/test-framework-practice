export class CheckoutStepTwoPage {
  constructor(page) {
    this.page = page;

    this.itemListNames = page.getByTestId('inventory-item-name');
    this.finishButton = page.getByTestId('finish');
  }

  async finish() {
    this.finishButton.click();
  }
}
