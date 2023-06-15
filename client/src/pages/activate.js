import { useState } from "react";
import Link from "next/link";
import axios from "axios";
import { useRouter } from "next/router";

export default function Login() {
  const [CNI, setCNI] = useState('')
    const [code, setcode] = useState('')
    const [error_list, setError_list] = useState([])
    const [invalid, setInvalid] = useState('')
    const router = useRouter();

    const submitActivate = (e) => {

        e.preventDefault();
        const data = {
            CNI: CNI,
            code: code
        }
        axios.get('/sanctum/csrf-cookie').then(response => {
            axios.post("/api/activate", data).then(res => {
                if (res.data.status === 200) {
                    localStorage.setItem("auth_token", res.data.token)
                    localStorage.setItem("auth_name", res.data.username)
                    localStorage.setItem("role", res.data.role)
                    if (res.data.role === 'admin') {
                        router.push("/");
                    }
                    else if (res.data.role === 'patrenaire') {
                        router.push("/");
                    }
                    else if (res.data.role === 'user') {
                        router.push("/");
                    }
                }
                else if (res.data.status === 401) {
                    setError_list(res.data.validation_errors)
                }
                else if (res.data.status === 403) {
                    setInvalid(res.data.message)
                    setError_list('/')
                }
            })
        })
}
  return (
    <div className="relative flex flex-col items-center justify-center min-h-screen overflow-hidden  bg-gradient-to-r from-white to-green-500">
      <div className="w-full p-6 bg-white rounded-xl shadow-md lg:max-w-xl">
      <img src="/logo.png" alt="Logo" className="mx-auto mb-6" width={80} />
        <form className="mt-6" onSubmit={submitActivate}>
          <div className="mb-4">
            <label
              htmlFor="CNI"
              className="block text-sm font-semibold text-gray-800"
            >
              CIN
            </label>
            <input
              type="text"
              value={CNI}
              onChange={(e) => setCNI(e.target.value)}
              className="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md focus:border-gray-400 focus:ring-gray-300 focus:outline-none focus:ring focus:ring-opacity-40"
            />
          </div>
          <div className="mb-2">
            <label
              htmlFor="code"
              className="block text-sm font-semibold text-gray-800"
            >
              Code Activation
            </label>
            <input
              type="text"
              value={code}
              onChange={(e) => setcode(e.target.value)}
              className="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md focus:border-gray-400 focus:ring-gray-300 focus:outline-none focus:ring focus:ring-opacity-40"
            />
          </div>
          <Link href="/forget"  className="text-xs text-blue-600 hover:underline">
              Renvoyez code
          </Link>
          <div className="mt-2">
            <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-green-600 rounded-md hover:bg-green-100 focus:outline-none focus:bg-gray-500">
              Activer compte
            </button>
          </div>
        </form>

        <p className="mt-4 text-sm text-center text-gray-700">
          Compte deja verifie?{" "}
          <Link href="/login" className="font-medium text-green-500 hover:underline">
              Login
          </Link>
        </p>
      </div>
    </div>
  );
}
