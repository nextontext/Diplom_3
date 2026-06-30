from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//p[normalize-space()='Конструктор']/parent::a",
    )
    CONSTRUCTOR_TITLE = (
        By.XPATH,
        "//h1[text()='Соберите бургер']",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[@href='/feed']",
    )
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']",
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Modal_modal__close')]",
    )
    FIRST_INGREDIENT_COUNTER = (
        By.XPATH,
        "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]//p[contains(@class, 'counter_counter__num')]",
    )
    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    BURGER_CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//ul[contains(@class, 'BurgerConstructor_basket__list')]",
    )
    FIRST_BUN_INGREDIENT = (
        By.XPATH,
        "(//img[contains(@src, 'bun')]/parent::a)[1]",
    )
    FIRST_BUN_INGREDIENT_COUNTER = (
        By.XPATH,
        "(//img[contains(@src, 'bun')]/parent::a)[1]//p[contains(@class, 'counter_counter__num')]",
    )

    FIRST_SAUCE_INGREDIENT = (
        By.XPATH,
        "(//img[contains(@src, 'sauce')]/parent::a)[1]",
    )
    FIRST_SAUCE_INGREDIENT_COUNTER = (
        By.XPATH,
        "(//img[contains(@src, 'sauce')]/parent::a)[1]//p[contains(@class, 'counter_counter__num')]",
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']",
    )
    ORDER_MODAL_IDENTIFIER_TEXT = (
        By.XPATH,
        "//p[text()='идентификатор заказа']",
    )
    ORDER_MODAL_NUMBER = (
        By.XPATH,
        "//p[text()='идентификатор заказа']/preceding-sibling::h2",
    )


