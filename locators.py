from selenium.webdriver.common.by import By


class AllNavLinks:

    MAIN_NAV_LINKS = (By.CSS_SELECTOR, ".menu-desktop__root > div >a")
    MAIN_NAV_LINKS_TEXT = ["Бытовая техника","Смартфоны и гаджеты","ТВ и мультимедиа","Компьютеры","Офис и сеть",
    "Отдых и развлечения","Инструменты","Строительство и ремонт","Дом, декор и кухня","Автотовары",
    "Аксессуары и услуги","Подарки"]

    SUB_NAV_LINKS = (By.CSS_SELECTOR, ".menu-desktop__root>div>div >a")
    SUB_NAV_LINKS_TEXT = ['для дома', 'уход за собой', 'планшеты', 'фототехника', 'аудио', 'видеоигры', 'комплектующие', 
    'ноутбуки', 'кресла', 'проекторы', 'электросамокаты', 'мангалы', 'аккумуляторные', 'садовые', 'электрика', 
    'сантехника', 'зоотовары', 'посуда', 'звук', 'автокресла', 'видеорегистраторы', 'наушники', 'мыши', 
    'свадьба', 'день рождения']


class CategoryLabels:
    CATEGORY_LABEL = (By.CSS_SELECTOR, ".container>ol>li>span")
    CATEGORY_LABEL_TEXT = ["Бытовая техникаfffff", "Смартфоны, планшеты и фототехника", "ТВ и мультимедиа",
    "Комплектующие, компьютеры и ноутбуки", "Офис и сеть", "Отдых и развлечения", "Инструменты",
    "Строительство и ремонт", "Дом, декор и кухня", "Автотовары", "Аксессуары и услуги",
    "Подарки"]

class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, "div.product-buy.product-buy_one-line > button.button-ui.buy-btn.button-ui_brand:nth-child(3)")
    CART_PRICE = (By.CSS_SELECTOR, ".cart-link__price")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-buy__price")