import json

def tsv2json(input_file, output_file):
    arr = []
    with open(input_file, 'r', encoding='utf-8') as file:
        # Skip the first line which contains the headers
        file.readline()
        for line in file:
            # Split the line by tabs and strip whitespace from each field
            fields = [field.strip() for field in line.split('\t')]
            # Create a dictionary for the current row
            data = {
                'Hotel Code': fields[0],
                'Image Url': fields[1],
                'Image Caption': fields[2],
                'Main Image': fields[3],
                'Image Type': fields[4]
            }
            # Append the dictionary to the list
            arr.append(data)
    
    # Write the list of dictionaries to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as output_file:
        json.dump(arr, output_file, indent=4)

# Driver Code
input_filename = 'D:\Python\code\grnc\hotel_image_map.tsv'
output_filename = 'D:\Python\code\grnc\hotel_image_map.json'
tsv2json(input_filename, output_filename)
