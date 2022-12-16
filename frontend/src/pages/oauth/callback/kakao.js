import { useEffect, useState } from "react";

const Kakao = () => {
  const [code, setcode] = useState("");
  // 인가코드
  useEffect(() => {
    setcode(new URL(window.location.href).searchParams.get("code"));
  }, []);
  console.log(code);
};

export default Kakao;
