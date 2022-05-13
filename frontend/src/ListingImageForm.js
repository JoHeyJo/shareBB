import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Alert from "./shared/Alert";
import ShareBBApi from "./api";

function ListingImageForm({changeImage, id}) {
  const [selectedFile, setSelectedFile] = useState();
  const [isFilePicked, setIsFilePicked] = useState(false);
  const navigate = useNavigate();
  const [alerts, setAlerts] = useState(null);

  async function addImage(id, imageData) {
    await ShareBBApi.listingImage(id, imageData);
  }

  /** Call parent function. */
  async function handleSubmit(evt) {
    evt.preventDefault();
    const formData = new FormData();
    formData.append('File', selectedFile);
    try {
      await addImage(id,formData); //TODO: id should be dynamic
      changeImage()
    } catch (err) {
      setAlerts([err]);
    }
  }

  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
    setIsFilePicked(true);
  };

  return (
    <form
      className="justify-content-center container bg-light mt-1 py-1"
      onSubmit={handleSubmit}
    >
      <input
        type="file"
        id="file"
        name="file"
        className="form-control"
        aria-label="file-url"
        onChange={changeHandler}
      />
      <div>

      {alerts && <Alert alerts={alerts} />}
      </div>
      <button className="btn-primary btn mt-3 py-1 btn-sm">
        Submit
      </button>
    </form>
  );
}
export default ListingImageForm;