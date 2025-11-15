import { PUBLIC_API_BASE_URL } from '$env/static/public';

export const uploadDoc = async (token: string, file: File) => {
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch(`${PUBLIC_API_BASE_URL}/documents`, {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${token}`
        },
        body: formData
    });

    return res.json();
};
