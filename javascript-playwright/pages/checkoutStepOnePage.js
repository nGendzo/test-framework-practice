export class CheckoutStepOnePage {
  constructor(page) {
    this.page = page;

    this.firstNameField = page.getByTestId('firstName');
    this.lastNameField = page.getByTestId('lastName');
    this.zipPostalCodeField = page.getByTestId('postalCode');
    this.continueButton = page.getByTestId('continue');
  }

  async fillCheckoutForm({ firstName, lastName, postalCode }) {
    await this.firstNameField.fill(firstName);
    await this.lastNameField.fill(lastName);
    await this.zipPostalCodeField.fill(postalCode);
  }

  async continue() {
    await this.continueButton.click();
  }
}
