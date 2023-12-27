import React, { useState } from 'react';
import axios from 'axios';

const YourComponent = () => {
  const [formData, setFormData] = useState({
    companyName: '',
    productDescription: '',
    productImage: null, // File type for image
    taglineText: '',
    theme: '',
    adType: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };


  const file = e.target.files[0];
    setFormData({
      ...formData,
      productImage: file
    });
  ;

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formDataToSend = new FormData();
    formDataToSend.append('companyName', formData.companyName);
    formDataToSend.append('productDescription', formData.productDescription);
    formDataToSend.append('productImage', formData.productImage);
    formDataToSend.append('taglineText', formData.taglineText);
    formDataToSend.append('theme', formData.theme);
    formDataToSend.append('adType', formData.adType);

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/endpoint', formDataToSend, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('Data sent successfully!', response.data);
      // Handle success or other logic
    } catch (error) {
      console.error('Error sending data:', error);
      // Handle error
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="companyName" value={formData.companyName} onChange={handleInputChange} placeholder="Company Name" /> <br />
      <textarea name="productDescription" value={formData.productDescription} onChange={handleInputChange} placeholder="Product Description" /><br />
      <input type="file" accept="image/*" onChange={handleImageChange} /><br />
      <input type="text" name="taglineText" value={formData.taglineText} onChange={handleInputChange} placeholder="Tagline Text" /><br />
      <input type="text" name="theme" value={formData.theme} onChange={handleInputChange} placeholder="Theme" /><br />
      <input type="text" name="adType" value={formData.adType} onChange={handleInputChange} placeholder="Ad Type" /><br />
      <button type="submit">Submit</button>
    </form>
  );
};


export default YourComponent;