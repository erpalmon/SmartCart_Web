// pages/index.js
import { useRouter } from 'next/router';

export default function Home() {
  const router = useRouter();

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>Welcome to SmartCart</h1>
      <p>Select an option to get started:</p>

      <div style={{ marginTop: '2rem' }}>
        <button
          onClick={() => router.push('/signup')}
          style={{
            marginRight: '1rem',
            padding: '0.5rem 1rem',
            fontSize: '1rem',
            cursor: 'pointer',
          }}
        >
          Sign Up
        </button>

        <button
          onClick={() => router.push('/login')}
          style={{
            padding: '0.5rem 1rem',
            fontSize: '1rem',
            cursor: 'pointer',
          }}
        >
          Login
        </button>
      </div>
    </div>
  );
}
