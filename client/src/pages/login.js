import { useState } from "react";
import Link from "next/link";
import axios from "axios";
import { useRouter } from "next/router";

export default function Login() {
  const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [error_list, setError_list] = useState([])
    const [invalid, setInvalid] = useState('')
    const router = useRouter();

    const submitLogin = (e) => {

        e.preventDefault();
        const data = {
            email: email,
            password: password
        }
        axios.get('/sanctum/csrf-cookie').then(response => {
            axios.post("/api/login", data).then(res => {
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
    <div className="relative flex flex-col items-center justify-center min-h-screen overflow-hidden  bg-gradient-to-r from-white to-green-600">
      <div className="w-full p-6 bg-white rounded-xl shadow-md lg:max-w-xl">
      <img src="/logo.png" alt="Logo" className="mx-auto mb-6" width={80} />
        <form className="mt-6" onSubmit={submitLogin}>
          <div className="mb-4">
            <label
              htmlFor="email"
              className="block text-sm font-semibold text-gray-800"
            >
              Email
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md focus:border-gray-400 focus:ring-gray-300 focus:outline-none focus:ring focus:ring-opacity-40"
            />
            <span className="text-muted fw-light">{error_list.email}</span>
          </div>
          <div className="mb-2">
            <label
              htmlFor="password"
              className="block text-sm font-semibold text-gray-800"
            >
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md focus:border-gray-400 focus:ring-gray-300 focus:outline-none focus:ring focus:ring-opacity-40"
            />
            <span className="text-muted fw-light">{error_list.email}</span>

          </div>
          <Link href="/forget"  className="text-xs text-blue-600 hover:underline">
              Renvoyez le code
          </Link>
          <div className="mt-2">
            <button className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-green-600 rounded-md hover:bg-green-400 focus:outline-none focus:bg-green-400">
              Login
            </button>
          </div>
        </form>

        <p className="mt-4 text-sm text-center text-gray-700">
          Se connecter pour la première fois?{" "}
          <Link href="activate" className="font-medium text-green-600 hover:underline">
              Activer votre compte
          </Link>
        </p>
      </div>
    </div>
  );
}
