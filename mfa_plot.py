import matplotlib.pyplot as plt

# Points (Usability, Security Strength)
labels = ['SMS', 'Push', 'Authenticator', 'Hardware']
x = [2, 4, 5, 8]
y = [3, 6, 7, 9]
colors = ['red', 'yellow', 'orange', 'green']

plt.figure(figsize=(6,4))
for i in range(len(labels)):
    plt.scatter(x[i], y[i], c=colors[i], s=200, label=labels[i])
    plt.text(x[i]+0.2, y[i]+0.2, labels[i], fontsize=12)

plt.xlabel('Usability (Low Friction → High Friction)')
plt.ylabel('Security Strength')
plt.title('Security-Usability Trade-off Matrix')
plt.grid(True)
plt.xlim(0,10)
plt.ylim(0,10)
plt.legend()
plt.tight_layout()
plt.savefig('security_usability_tradeoff.png')
plt.show()
