// image uploading and showing 
import React, { useState } from 'react';
import axios from 'axios';

const YourComponent = () => {
  const [image, setImage] = useState(null);

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('image', image);

    try {
      await axios.post('http://127.0.0.1:5000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('Image uploaded successfully');
      // You can handle success or perform additional operations here
    } catch (error) {
      console.error('Error uploading image:', error);
      // Handle error
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <button type="submit">Upload Image</button>
    </form>
  );
};

export default YourComponent;
