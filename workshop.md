201 Created (This is correct though)
  {
    "name": "Test Mouse",
    "price": 300.0,
    "quantity": 2,
    "currency": "SEK"
  }

201 Created (this is wrong)
{
    "name": "",
    "price": -24995.00,
    "quantity": -8,
    "currency": "SEK"
  }

201 Created (In price, it accepts e for "Euler)
  {
    "name": "Laptop\n\n\n\n\n",
    "price": 1e10,
    "quantity": 1,
    "currency": "SEK"
  }


201 Created (Tab Characters)
  {
    "name": "Acer Swift\t",
    "price": 16999.0,
    "quantity": 15,
    "currency": "SEK"
  }


201 Created (negative)

  {
    "name": "​",
    "price": -0.00,
    "quantity": -0,
    "currency": "SEK"
  }

201 Created (\r\n are valid string characters (just whitespace), trailing decimals)
    {
    "name": "MacBook Air\r\n",
    "price": 14999.00000,
    "quantity": 20,
    "currency": "SEK"
  }

422 Unprocessable Entity
  {
    "name": 12345,
    "price": "twenty-five thousand",
    "quantity": 8.5,
    "currency": 100
  }


422 Unprocessable Entity
 {
    "name": 404,
    "price": [19999, 20000],
    "quantity": "out of stock",
    "currency": false
  }

422 Unprocessable Entity

 {
    "name": "MacBook Pro",
    "price": NaN,
    "quantity": 999,
    "currency": "SEK"
 }