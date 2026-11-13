FROM python:3.11-slim

WORKDIR /app

COPY main.py test.py Inventory.py Product.py DigitalProduct.py PhysicalProduct.py CanBeShipped.py Supplier.py Order.py OrderLine.py ./

CMD ["python", "main.py"]