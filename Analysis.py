import tkinter as tk
from tkinter import messagebox, simpledialog
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function for sentiment analysis with vibrant effects
def analyze_sentiment():
    text = entry.get("1.0", "end-1c")  # Get input text
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter text to analyze.")
        return

    sentiment = analyzer.polarity_scores(text)
    polarity = sentiment["compound"]
    neutral = sentiment["neu"]
    pos = sentiment["pos"]
    neg = sentiment["neg"]

    # Determine sentiment and apply colors
    if polarity > 0:
        result_label.config(text="😊 Positive Sentiment!", fg="#4CAF50", bg="#E8F5E9")
    elif polarity == 0 or neutral > pos and neutral > neg:
        result_label.config(text="😐 Neutral Sentiment.", fg="#2196F3", bg="#E3F2FD")
    else:
        result_label.config(text="☹️ Negative Sentiment!", fg="#f44336", bg="#FFEBEE")

    # Show detailed sentiment scores
    details_label.config(text=f"Positive: {pos:.2f} | Neutral: {neutral:.2f} | Negative: {neg:.2f}", fg="#333")

# Function to clear the text and  results
def clear_text():
    entry.delete("1.0", "end")
    result_label.config(text="", bg="#f0f0f0")
    details_label.config(text="")

# Function to save results
def save_result():
    text = entry.get("1.0", "end-1c")
    result = result_label.cget("text")
    if not text.strip():
        messagebox.showwarning("Input Error", "Analyze text before saving.")
        return

    filename = simpledialog.askstring("Save Result", "Enter filename:")
    if filename:
        try:
            with open(f"{filename}.txt", "w") as file:
                file.write(f"Text: {text}\n\nSentiment Analysis Result:\n{result}")
            messagebox.showinfo("Saved!", f"Results saved as {filename}.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

# Set up UI
root = tk.Tk()
root.title("Sentiment Analysis - Vibrant Edition")
root.geometry("550x500")
root.config(bg="#f0f0f0")

# UI Elements
header = tk.Label(root, text="🌟 Sentiment Analysis Tool", font=("Helvetica", 18, "bold"), fg="#333", bg="#f0f0f0")
header.pack(pady=20)

instruction = tk.Label(root, text="Enter text for analysis:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")
instruction.pack(pady=10)

entry = tk.Text(root, width=55, height=5, font=("Helvetica", 12), bd=2, relief="solid")
entry.pack(pady=10)

# Buttons with vibrant styling
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment, font=("Helvetica", 12, "bold"),
                           bg="#4CAF50", fg="white", width=20, height=2, relief="raised")
analyze_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_text, font=("Helvetica", 12, "bold"), bg="#f44336", fg="white",
                         width=20, height=2, relief="raised")
clear_button.pack(pady=10)

save_button = tk.Button(root, text="Save Result", command=save_result, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white",
                        width=20, height=2, relief="raised")
save_button.pack(pady=10)

# Result labels
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
result_label.pack(pady=10)

details_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0", fg="#333", justify="left")
details_label.pack(pady=10)

# Run the app
root.mainloop()
