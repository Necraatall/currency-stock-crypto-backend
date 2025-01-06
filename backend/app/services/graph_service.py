import matplotlib.pyplot as plt
import io
import base64

async def generate_chart(data, title="Chart", x_label="X", y_label="Y"):
    plt.figure()
    plt.plot(data["x"], data["y"], marker="o")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)

    # Uložení grafu do paměti a jeho kódování do base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    buffer.close()
    plt.close()
    return image_base64
