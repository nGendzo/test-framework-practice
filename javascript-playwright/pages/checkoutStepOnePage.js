export class CheckoutStepOnePage {
  constructor(page) {
    this.page = page;

    this.firstNameField = page.getByTestId('firstName');
    this.lastNameField = page.getByTestId('lastName');
    this.zipPostalCodeField = page.getByTestId('postalCode');
    this.continueButton = page.getByTestId('continue');
  }

  async fillFirstNameField(firstName) {
    await this.FirstNameField.fill(firstName);
  }

  async fillLastNameField(lastName) {
    await this.lastNameField.fill(lastName);
  }

  async fillPostalCodeField(postalCode) {
    await this.lastNameField.fill(postalCode);
  }

  async clickContinueButton() {
    await this.continueButton.click;
  }
}
