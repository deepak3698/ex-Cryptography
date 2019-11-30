input_val="meri jaan"

list1=[5,9,12,16,18,22,17,45,84,134,234,146,275,246,232,123,304,307,301,312,305,308,328,322]
list1=list(dict.fromkeys(list1))

encrypt="dashfgukdikjnbzdnvdezfbdvdfkajfvszhdbcsbcgsjdda" \
        "hgfkgzvhfIfgjADHSBFVAJDGVSDJGABSgaXSHBVCAJDGHSVAJFSDVagdVASDGfdfgdshfsghgjgffhg" \
        "fhfsdjfdsggfjsdgfjsdgfhdsgffhakjfgjasmbdgjdjszfvhdjdgvszhsfjjfdbzvhgsdvhashdchgaSDFhagdcHADCaghcxhsgd" \
        "vcshgAHvSCHDVSChgjfthfhffjHGSHdasgfgdsfjksdhfgkdbmvfszjfdszvhszdhfmhesbjhvdnbfvzgfjjfgjgjfgjfdsmfbd"

encrypt=list(encrypt)

for i,j in enumerate(input_val):
    encrypt[list1[i]]=j
encrypt="".join(encrypt)

with open("st.jpg","w") as op:
    op.write(encrypt)
    op.write("\n")
    op.write(str(len(input_val)))




