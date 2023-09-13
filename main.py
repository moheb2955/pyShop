import aspose.words as aw
import aspose.pydrawing as drawing

# Load the license
wordLic = aw.License()
wordLic.set_license("Aspose.Total.lic")

# Load the DOC file
doc = aw.Document("Figma VS Adobe xd.docx")

# Get the custom properties collection and clear them
custProps = doc.custom_document_properties
custProps.clear()

# Get the built-in properties collection and clear them
builtInProps = doc.built_in_document_properties
builtInProps.clear()

# Save the Word file
doc.save("Output.doc")

print ("Metadata removed from the Word file")