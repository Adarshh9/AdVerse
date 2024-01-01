import React from 'react';

const ImageDisplay = ({ imageId }) => {
  // Replace 'http://localhost:5000' with the URL where your Flask backend is running
  const imageUrl = `http://localhost:5000/api/images/${imageId}`;
  const testurl = 'https://ag-spots-2016.o.auroraobjects.eu/2016/12/28/other/2880-1800-crop-nissan-skyline-r34-gt-r-c638828122016174701_1.jpg  '
  return (
    <div>
      <h2 style={{textAlign:'center'}}>Displayed Image:</h2><br/><br/><br/>
      <img src={testurl} alt="Displayed Image" style={{maxWidth:'500px' , maxHeight:'700px'}}/>
      <br/><br/><br/><br/>
    </div> 
  );
};

export default ImageDisplay;
