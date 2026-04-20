export class CheckoutCompletePage {
  constructor(page) {
    this.page = page;

    this.completionHeaderText = page.getByTestId('complete-header');
  }
}
