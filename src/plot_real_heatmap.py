import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set publication style
plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

# Read real dataset
csv_path = r'B:\SERENE_REQ_Paper\SERENE_REQ_Dataset.csv'
df = pd.read_csv(csv_path)

# Build cross-tabulation matrix between Domain and NFR_Class
ct = pd.crosstab(df['Domain'], df['NFR_Class'])

# Map full names for display
domain_labels = {
    'Cloud': 'Cloud Native & Infra',
    'Energy': 'Smart Grid & Energy',
    'FinTech': 'FinTech & Banking',
    'Healthcare': 'IoMT & Medical',
    'IoT': 'IoT & Edge Devices',
    'Security': 'Cybersecurity & Auth'
}

class_labels = {
    'EN': 'Energy (EN)',
    'MN': 'Maintainability (MN)',
    'PE': 'Performance (PE)',
    'PO': 'Portability (PO)',
    'RE': 'Reliability (RE)',
    'SE': 'Security (SE)',
    'US': 'Usability (US)'
}

ct.index = [domain_labels.get(d, d) for d in ct.index]
ct.columns = [class_labels.get(c, c) for c in ct.columns]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Custom color palette (Viridis/YlGnBu professional gradient)
sns.heatmap(
    ct, 
    annot=True, 
    fmt='d', 
    cmap='YlGnBu', 
    cbar_kws={'label': 'Verified GitHub Requirement Count'}, 
    linewidths=1.5, 
    linecolor='white',
    ax=ax,
    annot_kws={'size': 12, 'weight': 'bold'}
)

ax.set_title('SERENE-REQ: Real Traceability Matrix (Domain vs. ISO NFR Class)', fontsize=14, pad=15, weight='bold')
ax.set_xlabel('ISO/IEC 25010 Quality Characteristics (NFR Class)', fontsize=12, labelpad=10, weight='bold')
ax.set_ylabel('Enterprise Industry Domains', fontsize=12, labelpad=10, weight='bold')

plt.xticks(rotation=30, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)

plt.tight_layout()

# Save to figures directory
output_dir = r'B:\SERENE_REQ_Paper\figures'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'Fig3_Traceability_Heatmap.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()

print(f"Heatmap generated successfully and saved to: {output_path}")
