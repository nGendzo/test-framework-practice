import { test, expect } from '@playwright/test';
import { products } from '../data/products';
import { InventoryPage } from '../pages/inventoryPage';
import { CartPage } from '../pages/cartPage';
import { ProductPage } from '../pages/productPage';
import { CheckoutStepOnePage } from '../pages/checkoutStepOnePage';
import { CheckoutStepTwoPage } from '../pages/checkoutStepTwoPage';
import { CheckoutCompletePage } from '../pages/checkoutCompletePage';

test.describe('main flows', async () => {
  let inventoryPage;
  let cartPage;
  let productPage;
  let checkoutStepOnePage;
  let checkoutStepTwoPage;
  let checkoutCompletePage;

  test.beforeEach('POM setup', async ({ page }) => {
    inventoryPage = new InventoryPage(page);
    cartPage = new CartPage(page);
    productPage = new ProductPage(page);
    checkoutStepOnePage = new CheckoutStepOnePage(page);
    checkoutStepTwoPage = new CheckoutStepTwoPage(page);
    checkoutCompletePage = new CheckoutCompletePage(page);

    await inventoryPage.open();
  });

  test('open burger menu @regression', async () => {
    await inventoryPage.openBurgerMenu();

    await expect(inventoryPage.burgerMenuItemList).toBeVisible();
  });

  test('open "Sauce Labs Backpack" and add to cart @regression', async () => {
    await inventoryPage.openItem(products.sauceLabsBackpack.name);
    await productPage.addToCart();
    await productPage.openCart();

    await expect(cartPage.itemListNames).toHaveText(
      products.sauceLabsBackpack.name,
    );
  });

  test('open "T-Shirt (Red)" and add to cart @regression', async () => {
    await inventoryPage.openItem(products.tShirtRed.name);
    await productPage.addToCart();
    await productPage.openCart();

    await expect(cartPage.itemListNames).toHaveText(products.tShirtRed.name);
  });

  test('open two items and add them to cart @regression', async () => {
    await inventoryPage.openItem(products.sauceLabsBikeLight.name);
    await productPage.addToCart();
    await productPage.goToInventory();
    await inventoryPage.openItem(products.sauceLabsBoltTShirt.name);
    await productPage.addToCart();
    await productPage.openCart();

    await expect(cartPage.itemListNames).toHaveText([
      products.sauceLabsBikeLight.name,
      products.sauceLabsBoltTShirt.name,
    ]);
  });

  test.only('buy an item @e2e', async () => {
    await inventoryPage.openItem(products.sauceLabsOnesie.name);
    await productPage.addToCart();
    await productPage.openCart();
    await cartPage.checkout();
    await checkoutStepOnePage.fillFirstNameField('Walter');
    await checkoutStepOnePage.fillLastNameField('White');
    await checkoutStepOnePage.fillPostalCodeField('1234');
    await checkoutStepOnePage.continue();
    await checkoutStepTwoPage.finish();

    await expect(checkoutCompletePage.completionHeaderText).toHaveText(
      'Thank you for your order!',
    );
  });
});
