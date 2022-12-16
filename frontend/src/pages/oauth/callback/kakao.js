import { useEffect, useState } from "react";
import axios from "axios";
import { backUrl } from "../../../config/config";
import Router from "next/router"

let mountCount = 1;
const Kakao = () => {
  const [code, setcode] = useState("");
  const [didMount, setDidMount] = useState(false);

  useEffect(() => {
    setcode(new URL(window.location.href).searchParams.get("code"));
  }, []);

  if (code && !didMount){
    mountCount++;
    setDidMount(true);
    axios
        .get(`${backUrl}/accounts/login/kakao?code=${code}`,{
          params : {
            code : code
          }
        })
        .then((res) => {
          console.log(res.data);
          return Router.push('/')
        })
        .catch(err => console.error(err.message));
      }
};

export default Kakao;
