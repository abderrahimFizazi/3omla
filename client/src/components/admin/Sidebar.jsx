import Link from "next/link";
import {AiOutlineUser} from "react-icons/ai"
import {FiSettings} from "react-icons/fi"
import {CiMoneyBill} from "react-icons/ci"
const Sidebar = () => {
  return (
    <aside className="bg-white-800 text-black w-80 min-h-screen shadow-2xl">
      <img src="/logo.png" alt="Logo" className="mx-auto " width={50} />
      <div className="flex items-center justify-center h-16 border-b border-gray-700">
        <h1 className="text-xl font-bold">Admin Dashboard</h1>
      </div>
      
      {/* Navigation Links */}
      <nav className="mt-4">
        <ul>
          <li>
            <Link href="/dashboard" className="flex items-center py-2 px-4 hover:bg-green-500 hover:text-white">
                <AiOutlineUser className="w-10"/>
                Gestion des clients
            </Link>
          </li>
          <li>
            <Link href="/users" className="flex items-center py-2 px-4 hover:bg-green-500 hover:text-white">
                <FiSettings className="w-10"/>
                Gestion des services
            </Link>
          </li>
          <li>
          <Link href="/users" className="flex items-center py-2 px-4 hover:bg-green-500 hover:text-white">
                <CiMoneyBill className="w-10"/>
                Gestion des Payements
            </Link>
          </li>
        </ul>
      </nav>
      
    </aside>
  );
};

export default Sidebar;
