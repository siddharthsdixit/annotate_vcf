# README: VCF Gene Annotation Script

## Overview
This Python script annotates a **VCF (Variant Call Format) file** by adding gene names based on **BED (Browser Extensible Data) file** regions. It checks which **gene(s) correspond** to each variant position and updates the VCF file accordingly.

---

## File Requirements
- **VCF File**: Must have a `#CHROM` column in the header.
- **BED File**: Should have **no header** and be in the format:
  ```
  chrom    start    end    gene
  ```
  Example BED:
  ```
  chr1    16200589    16200879    MSI
  chr14   105241300   105241400   gene1
  ```
- The **script will add a "GENE" column** to the output VCF file.

---

## Prerequisites
### 1. Install Python
Ensure you have **Python 3.7+** installed. You can check by running:
```bash
python --version
```

### 2. Install Required Libraries
This script uses **Pandas** for data handling. Install it using:
```bash
pip install pandas
```

---

## Usage
### 1. Set File Paths
Open the script and **edit these file paths** at the top:
```python
bed_file = "your_bed_file.bed"
vcf_file = "your_vcf_file.vcf"
output_file = "annotated_variants.vcf"
```

### 2. Run the Script
Simply execute the script using:
```bash
python annotate_vcf.py
```

### 3. Output
A new **annotated VCF file** will be generated:
```
annotated_variants.vcf
```
It will include a **GENE** column.

---

## Input & Output Example
### Input VCF File
```
#CHROM   POS        ID  REF                  ALT
chr14    105241392  .   GCCCCACCGCCCCGGCCCCA G
chr14    105241339  .   TCCTGTAAAGCAGGGCTG    T
```
### Input BED File
```
chr14    105241300  105241400  gene1
chr14    105241320  105241350  gene2
```
### Output Annotated VCF
```
#CHROM   POS        ID  REF                  ALT   GENE
chr14    105241392  .   GCCCCACCGCCCCGGCCCCA G     gene1
chr14    105241339  .   TCCTGTAAAGCAGGGCTG    T     gene2
```

---

## Notes
- The script handles **multiple overlapping genes** by merging them with a comma (`,`).
- The **output VCF file keeps the original format** and adds a `GENE` column.
- If **no gene is found**, the script marks it as `"."`.

---

## Troubleshooting
### Error: "Missing '#CHROM' column"
   - Ensure your VCF file **has a correct header**.
   - The script auto-detects the `#CHROM` row, but if it's missing, check the file.

### Error: "No matching gene found"
   - Check if the **positions in the VCF file match** any range in the BED file.

### Error: Pandas Not Found
   - Install it using:
     ```bash
     pip install pandas
     ```

---

## Summary
| Feature            | Description |
|--------------------|-------------|
| 📂 **Input Files** | VCF, BED |
| 📝 **Output File** | Annotated VCF |
| 🛠 **Dependencies** | Python (3.7+), Pandas |
| 🚀 **Usage** | `python annotate_vcf.py` |
| 🎯 **Functionality** | Adds genes based on VCF positions |

---

## Need Help?
If you run into issues, check:
- File formatting (headers, tab-separated values)
- Installed dependencies (`pandas`)

✅ **Now you have everything you need to use the script anytime!** 🚀

