import pandas as pd

# Specify file paths here
bed_file = "SA74_Targets_SNP_CNV_manifest_20bpPad_smerged.bed"  # Replace with your BED file path
vcf_file = "FFP-2025-07304_TRID-2025-05301_S309_NovaSeqXPlus-Run0117.vcf"  # Replace with your VCF file path
output_file = "annotated_variants.vcf"  # Output file

def load_bed_file(bed_file):
    """Load BED file into a Pandas DataFrame."""
    bed_cols = ["chrom", "start", "end", "gene"]
    bed_df = pd.read_csv(bed_file, sep="\t", names=bed_cols, header=None)
    return bed_df

def load_vcf_file(vcf_file):
    """Load VCF file into a Pandas DataFrame, ensuring the correct #CHROM column is used."""
    try:
        # Read the VCF file to find the correct header line
        with open(vcf_file, "r") as f:
            for line in f:
                if line.startswith("#CHROM"):
                    header = line.strip().split("\t")  # Extract correct column names
                    break
            else:
                raise ValueError("VCF file format error: No '#CHROM' header found.")

        # Load the VCF file with correct headers
        vcf_df = pd.read_csv(vcf_file, sep="\t", comment="#", header=None, names=header, dtype=str)
        
        print("VCF Columns Detected Before Renaming:", vcf_df.columns)

        if "#CHROM" not in vcf_df.columns:
            raise ValueError("VCF file format error: Missing '#CHROM' column. Check the file.")

        # Rename for easier handling
        vcf_df.rename(columns={"#CHROM": "chrom", "POS": "pos"}, inplace=True)
        print("VCF Columns After Renaming:", vcf_df.columns)

        return vcf_df

    except Exception as e:
        print(f"Error loading VCF file: {e}")
        exit(1)

def annotate_vcf_with_genes(bed_df, vcf_df, output_file):
    """Annotate the VCF file by adding the corresponding gene from the BED file."""
    
    vcf_df["GENE"] = "."

    for idx, row in vcf_df.iterrows():
        chrom, pos = row["chrom"], int(row["pos"])  # Ensure POS is integer
        matches = bed_df[(bed_df["chrom"] == chrom) & (bed_df["start"] <= pos) & (bed_df["end"] >= pos)]
        
        if not matches.empty:
            vcf_df.at[idx, "GENE"] = ",".join(matches["gene"])  # Handle multiple overlapping genes

    # Rename 'chrom' back to '#CHROM' for correct VCF format
    vcf_df.rename(columns={"chrom": "#CHROM"}, inplace=True)

    # Save the updated VCF file with gene annotations
    vcf_df.to_csv(output_file, sep="\t", index=False)
    print(f"✅ Annotated VCF saved to {output_file}")

# Run the script
print("🔍 Loading BED and VCF files...")
bed_df = load_bed_file(bed_file)
vcf_df = load_vcf_file(vcf_file)

print("📝 Annotating VCF file with gene names...")
annotate_vcf_with_genes(bed_df, vcf_df, output_file)

