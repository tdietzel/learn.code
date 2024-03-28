import './globals.css'
import { Inter } from 'next/font/google'
import Link from 'next/link'

const inter = Inter({ subsets: ['latin'] }) // Google font: change here and line 2 & 14

export const metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <nav>
          <Link href="/Home" >Home</Link> | <Link href="/Games/Blackjack">Games</Link>
        </nav>
        {children}</body>
    </html>
  )
}