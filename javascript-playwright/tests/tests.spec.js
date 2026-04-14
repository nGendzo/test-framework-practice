import { test, expect } from '@playwright/test';
import { products } from '../data/products';
import { InventoryPage } from '../pages/inventoryPage';
import { CartPage } from '../pages/cartPage';
import { ProductPage } from '../pages/productPage';

test.describe('main flows', async () => {
  let inventoryPage;
  let cartPage;
  let productPage;

  test.beforeEach('POM setup', async ({ page }) => {
    inventoryPage = new InventoryPage(page);
    cartPage = new CartPage(page);
    productPage = new ProductPage(page);
    await inventoryPage.open();
  });

  test('open burger menu @regression', async () => {
    await inventoryPage.openBurgerMenu();

    await expect(inventoryPage.burgerMenuItemList).toBeVisible();
  });

  test('open "Sauce Labs Backpack" and add to cart @regression', async () => {
    await inventoryPage.openItem(products.sauceLabsBackpack.name);
    await productPage.addToCart();
    await cartPage.open();

    await expect(cartPage.itemListNames).toHaveText(
      products.sauceLabsBackpack.name,
    );
  });

  test('open "T-Shirt (Red)" and add to cart @regression', async () => {
    await inventoryPage.openItem(products.tShirtRed.name);
    await productPage.addToCart();
    await cartPage.open();

    await expect(cartPage.itemListNames).toHaveText(products.tShirtRed.name);
  });

  test('open two items and add them to cart @regression', async () => {
    await inventoryPage.openItem(products.sauceLabsBikeLight.name);
    await productPage.addToCart();
    await inventoryPage.open();
    await inventoryPage.openItem(products.sauceLabsBoltTShirt.name);
    await productPage.addToCart();
    await cartPage.open();

    await expect(cartPage.itemListNames).toHaveText([
      products.sauceLabsBikeLight.name,
      products.sauceLabsBoltTShirt.name,
    ]);
  });
});
