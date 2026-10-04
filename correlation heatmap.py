import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ১. শিক্ষার্থীদের পড়ার সময়, উপস্থিতি ও স্কোরের ডামি ডেটাসেট
data = {
    'Study_Hours': [2, 4, 5, 7, 8, 10],
    'Attendance_%': [60, 70, 75, 85, 90, 98],
    'Exam_Score': [50, 60, 65, 80, 85, 95],
    'Sleep_Hours': [8, 7, 7, 6, 6, 5],
}

df = pd.DataFrame(data)

# ২. ডাটাসেটের Correlation Matrix তৈরি
correlation_matrix = df.corr()

# ৩. Seaborn দিয়ে Heatmap তৈরি
plt.figure(figsize=(7, 5))
sns.heatmap(
    correlation_matrix,
    annot=True,  # প্রতিটি ঘরে সংখ্যা (Correlation Value) দেখাবে
    cmap='coolwarm',  # সুন্দর কালার স্কিম (লাল-নীল থিম)
    fmt='.2f',  # দশমিকের পর ২ ঘর পর্যন্ত দেখাবে
    linewidths=0.5,  # ঘরগুলোর মাঝের বর্ডার
)

plt.title('Student Performance Correlation Heatmap')
plt.show()