import { chromium } from '@playwright/test';

export default async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'secret_sauce');
  await page.click('#login-button');

  await page.waitForSelector('[data-test="title"]');

  await page.context().storageState({ path: 'storageState.json' });

  console.log('Login Successful, storageState saved!');
  await browser.close();
};
