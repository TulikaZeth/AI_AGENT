# # test_opencv_tool.py
# from tools.opencv_tool import OpenCVTool
# import cv2
# import matplotlib.pyplot as plt

# # Initialize tool
# tool = OpenCVTool()

# # Set test image path (update this!)
# image_path = "image.png"  # Make sure this file exists

# # Preprocess image
# try:
#     processed_img = tool.preprocess_image(image_path)
    
#     # Show processed image
#     plt.imshow(processed_img)
#     plt.title("Preprocessed Image")
#     plt.axis('off')
#     plt.show()
    
#     # Convert to base64
#     b64_img = tool.image_to_base64(processed_img)
#     print("✅ Image successfully converted to base64.")
#     print(f"Base64 preview (first 100 chars): {b64_img[:100]}...")

# except Exception as e:
#     print(f"❌ Error: {e}")

# ----------------------------------this is for testing my gemini tool
# from tools.gemini_tool import GeminiTool
# from tools.opencv_tool import OpenCVTool

# # Prepare image
# opencv = OpenCVTool()
# processed = opencv.preprocess_image("image.png")
# base64_img = opencv.image_to_base64(processed)

# # Analyze with Gemini
# gemini = GeminiTool()
# result = gemini.analyze_crop_image(base64_img, crop_name="")
# print(result)


# # ============THIS IS FOR TESTING MY DIAGNOSIS AGENT=====
# from agents.diagnosis_agent import DiagnosisAgent
# from tools.opencv_tool import OpenCVTool

# opencv= OpenCVTool()
# img=opencv.preprocess_image("image.png")
# base64_img=opencv.image_to_base64(img)

# agent=DiagnosisAgent()
# result=agent.run(base64_img,crop_name="")

# print("Result")
# print(result)




# =======TEST diagnosis agent again!

# test_diagnosis_agent.py

# from tools.opencv_tool import OpenCVTool
# from agents.diagnosis_agent import DiagnosisAgent

# # Initialize tools
# opencv = OpenCVTool()
# agent = DiagnosisAgent()

# image_path = "image.png"  
# try:
#     processed = opencv.preprocess_image(image_path)
#     base64_img = opencv.image_to_base64(processed)

#     # Run diagnosis
#     result = agent.run(base64_img, crop_name="")  
#     print("Diagnosis Result:\n")
#     print(result)

# except Exception as e:
#     print(f"Error: {e}")


# +=======testing serper tool=======
# from tools.serper_tool import SerperTool

# serper = SerperTool()
# query = "Best treatement for scabies"
# results = serper.search(query)

# print("Serper Results:\n")
# print(results)


# test_opencv.py
from tools.opencv_tool import OpenCVTool  

def main():
    tool = OpenCVTool()
    tool.process_live_camera()

if __name__ == "__main__":
    main()
