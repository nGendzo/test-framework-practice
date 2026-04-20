export class CheckoutStepTwoPage {
  constructor(page) {
    this.page = page;

    this.itemNames = page.getByTestId('inventory-item-name');
    this.finishButton = page.getByTestId('finish');
  }

  async clickFinishButton() {
    this.finishButton.click();
  }
}
