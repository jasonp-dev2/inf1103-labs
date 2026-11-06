FROM python:3.11-slim

WORKDIR /app

COPY inventory_manager.py Inventory.py Product.py DigitalProduct.py PhysicalProduct.py CanBeShipped.py ./

CMD ["python", "inventory_manager.py"]

#build with inf1103-lab7-smart-auditor
#run using docker run --rm -it -v "${PWD}:/app" -w /app inf1103-lab8-smart-auditor