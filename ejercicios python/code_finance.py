import mplfinance as mpf
import yfinance as yf

data = yf.download('AAPL', period="5d", interval="30m", auto_adjust=False)

if data.empty:
    print("No se pudieron obtener datos para AAPL.")
else:
    print(data.columns)  # verificar el orden real antes de aplanar
    data.columns = data.columns.get_level_values(0)
    data = data.dropna()

    mpf.plot(data, type='candle', volume=True, style='charles', title='AAPL')
