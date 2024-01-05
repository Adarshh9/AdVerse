import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const YourComponent = () => {
  const [formData, setFormData] = useState({
    companyName: '',
    productDescription: '',
    productImage: null,
    taglineText: '',
    theme: '',
    adType: '',
  });
 
   

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };


  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setFormData({
      ...formData,
      productImage: file
    });
  };

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
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  return (
    <div style={{ textAlign: 'centre', margin: '10px'  }}> 
    <div style={{ textAlign:'center', color:'blue', fontWeight:'bold', fontStyle:'italic', fontSize:'30px' }}><h1>ADVerse</h1></div><br />
      <form onSubmit={handleSubmit} style={{  maxWidth: '500px', margin: 'auto', padding: '10px', border: '1px solid #ccc', borderRadius: '8px',backgroundColor:'#00FFFF',textAlign: 'Left' }}>
      <li>
         <b>Company Name :&nbsp;&nbsp; </b> 
          <input type="text" name="companyName" value={formData.companyName} onChange={handleInputChange} style={{border: '2px solid #ccc' , borderRadius: '8px'}}   />
        </li><br />
        <li>
          <b>Product Description :&nbsp;&nbsp;</b>
          <textarea name="productDescription" value={formData.productDescription} onChange={handleInputChange} style={{border: '2px solid #ccc' , borderRadius: '8px'}} />
        </li><br />
        <li>
         <b>
         Upload File   :  
          <input type="file" accept="image/*" onChange={handleImageChange} />
         </b>
        </li><br />
        <li>
          <b>Tagline Text :&nbsp;&nbsp;</b>
          <input type="text" name="taglineText" value={formData.taglineText} onChange={handleInputChange} style={{border: '2px solid #ccc' , borderRadius: '8px'}} />
        </li><br />
        <li>
          <b>Theme :&nbsp;&nbsp;</b>
          <input type="text" name="theme" value={formData.theme} onChange={handleInputChange} style={{border: '2px solid #ccc' , borderRadius: '8px'}} />
        </li><br />
        <li>
          <b>Ad Type :&nbsp;&nbsp;</b>
          <input type="text" name="adType" value={formData.adType} onChange={handleInputChange} style={{border: '2px solid #ccc' , borderRadius: '8px'}}  />
        </li><br />
            
            <button type="submit"style={{ padding: '10px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>Submit</button>
            
              </form>
      <div style={{ textAlign: 'center', margin: '5px' }}>
        <Link to="/product">
          <button style={{ padding: '10px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
            Get your image
          </button>
        </Link>
      </div>
    </div>
  );
};

export default YourComponent;
